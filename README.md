# Funcionario Finder - Unified Transparency Engine 🕵️‍♂️🏛️

> **Architect: Alejandro Ramírez**

A comprehensive investigative platform for government transparency, relationship mapping, and public official auditing in Paraguay.

## 🚀 Overview
Funcionario Finder is the unified evolution of the "Transparency Utilities" suite. It aggregates data from multiple institutional portals, maps relationships between high-ranking officials, and calculates a proprietary **Corruption Risk Index** based on salary outliers, position seniority, and media exposure.

## ✨ Key Features
- **Centralized Data Scraping**: Automated ingestion of payroll records from the Ministry of Finance.
- **Relationship Mapping**: Identifies connections and potential "dealings" between officials within and across departments.
- **Corruption Risk Index (CRI)**: An automated 0-100 scoring system using weighted data points from media surveillance and financial records.
- **Media Surveillance Engine**: Real-time correlation of official profiles with corruption-related news articles.
- **Source Transparency**: Comprehensive listing of all institutional data sources used for aggregation.

## 🛠️ Tech Stack
- **Backend**: Flask, Flask-Caching
- **Intelligence**: Custom Risk Assessment & Graph Logic
- **Data Acquisition**: Multi-source scrapers (Hacienda, NewsAPI)
- **API**: RESTful interface with enriched JSON payloads.

## 📂 Project Structure
- `backend/app.py`: Main API entry point.
- `backend/intelligence.py`: Risk calculation and connection logic.
- `backend/scraping/`: Specialized modules for data extraction.
- `frontend/`: Integrated UI for data visualization.

## 📊 Data Sources
The platform currently aggregates data from:
1.  **Hacienda Open Data**: Nominal payroll and salary data.
2.  **NewsAPI**: Media monitoring for corruption and administrative investigation keywords.
3.  **DNCP**: (In Development) Public procurement and contract awards.

---
*Created with precision by Alejandro Ramírez.*
