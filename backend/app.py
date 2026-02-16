"""
 * Author: Alejandro Ramírez
 * Project: funcionario-finder
 * Logic: Transparency API for querying public official data, integrating \n * multi-source scraping, news surveillance, and automated corruption risk assessment.
 """

from flask import Flask, jsonify, request
from flask_caching import Cache
from scraping.funcionarios import obtener_funcionarios
from scraping.noticias import buscar_noticias
from intelligence import CorruptionAuditLogic as CorruptionAudit

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
audit_engine = CorruptionAudit()

# Source Registry
DATA_SOURCES = [
    {"name": "Hacienda Open Data", "url": "https://datos.hacienda.gov.py/nomina", "type": "Financial/Payroll"},
    {"name": "NewsAPI", "url": "https://newsapi.org", "type": "Media Surveillance"},
    {"name": "DNCP", "url": "https://www.contrataciones.gov.py", "type": "Procurement/Contracting (Upcoming)"}
]

@app.route('/api/sources', methods=['GET'])
def get_sources():
    """Lists all data sources used for aggregation."""
    return jsonify(DATA_SOURCES)

@app.route('/api/funcionarios', methods=['GET'])
@cache.cached(timeout=300, query_string=True)
def get_funcionarios():
    """
    Retrieves officials with enrichment:
    - Corruption Risk Index
    - Relationship Mapping (Dealings)
    """
    departamento = request.args.get('departamento')
    all_funcionarios = obtener_funcionarios()
    
    # Filter if needed
    filtered = all_funcionarios
    if departamento:
        filtered = [f for f in all_funcionarios if f.get('departamento', '').lower() == departamento.lower()]
        
    # Enrichment pass
    enriched_results = []
    for f in filtered[:50]: # Process top 50 for performance in this unified version
        news = buscar_noticias(f)
        risk_index = audit_engine.calculate_index(f, len(news))
        dealings = audit_engine.find_dealings(f, all_funcionarios)
        
        f['corruption_index'] = risk_index
        f['dealings'] = dealings
        f['news'] = news
        enriched_results.append(f)
        
    return jsonify(enriched_results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
