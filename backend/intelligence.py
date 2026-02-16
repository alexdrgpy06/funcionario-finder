"""
Author: Alejandro Ramírez

Corruption Intelligence Engine
Computes risk indices and maps relationships between public officials
based on multi-source data points.
"""

class CorruptionAudit:
    def __init__(self):
        # Weighting factors for the index
        self.WEIGHTS = {
            "news_exposure": 0.4,
            "salary_outlier": 0.3,
            "position_risk": 0.3
        }
        
        # High-risk keywords in job titles
        self.RISK_POSITIONS = ["director", "ministro", "coordinador", "compras", "licitaciones"]

    def calculate_index(self, official_data, news_count):
        """
        Calculates a corruption risk index from 0 to 100.
        """
        # 1. News Exposure Score (max 40 pts)
        # More news hits for 'corruption' + official name = higher score
        news_score = min(news_count * 5, 40)
        
        # 2. Position Risk Score (max 30 pts)
        pos_score = 0
        cargo = official_data.get('cargo', '').lower()
        if any(keyword in cargo for keyword in self.RISK_POSITIONS):
            pos_score = 30
            
        # 3. Salary Outlier (Simplified logic for now - max 30 pts)
        # In a full implementation, this would compare against median for the department
        salary = official_data.get('salario', 0) or 0
        salary_score = 0
        if salary > 20000000: # 20M Gs as a baseline high-salary threshold
            salary_score = 30
            
        final_index = news_score + pos_score + salary_score
        return round(min(final_index, 100), 2)

    def find_dealings(self, official, all_officials):
        """
        Identifies potential dealings between officials.
        Currently connects by same institution/department.
        """
        dept = official.get('departamento')
        if not dept:
            return []
            
        # Connect to others in the same department (excluding self)
        connections = [
            {"nombre": f.get('nombre'), "relacion": "Same Department"}
            for f in all_officials 
            if f.get('departamento') == dept and f.get('nombre') != official.get('nombre')
        ]
        
        return connections[:10] # Limit to top 10 connections for performance
