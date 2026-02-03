# 🚗 WAY AI Services

**렌터카 플랫폼을 위한 AI 마이크로서비스**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📋 목차

- [개요](#-개요)
- [시스템 아키텍처](#-시스템-아키텍처)
- [AI 서비스](#-ai-서비스)
- [데이터 플로우](#-데이터-플로우)
- [기술 스택](#-기술-스택)
- [빠른 시작](#-빠른-시작)
- [API 문서](#-api-문서)
- [프로젝트 구조](#-프로젝트-구조)
- [개발 로드맵](#-개발-로드맵)

---

## 🎯 개요

WAY AI Services는 렌터카 플랫폼의 핵심 AI 기능을 제공하는 마이크로서비스입니다.

### 주요 기능

| 서비스 | 설명 | 핵심 기술 |
|--------|------|----------|
| 🎯 **추천 엔진** | 개인화된 차량 추천 | CF/CBF, Embedding, ALS |
| 💬 **AI 챗봇** | 자연어 기반 고객 상담 | RAG, LangChain, Vector DB |
| 💰 **가격 예측** | 동적 가격 최적화 | XGBoost, Prophet |
| 📊 **행동 분석** | 고객 행동 인사이트 | Funnel, Cohort, Segment |

---

## 🏗 시스템 아키텍처
────────────┘


```mermaid
graph TB
    subgraph Client
        A[Mobile/Web/Admin]
    end
    
    subgraph Gateway
        B[Spring Boot :8080]
    end
    
    subgraph AI Services
        C[FastAPI :8000]
        D[추천엔진]
        E[챗봇]
        F[가격예측]
        G[행동분석]
    end
    
    subgraph Storage
        H[(MySQL)]
        I[(Redis)]
        J[(Qdrant)]
        K[Kafka]
    end
    
    A -->|HTTPS| B
    B -->|REST| C
    C --> D & E & F & G
    D & E & F & G --> H & I & J & K
<img width="1220" height="750" alt="diagram" src="https://github.com/user-attachments/assets/8a050e19-7038-4a39-a215-037e38c8a518" />

<img width="1090" height="750" alt="diagram (1)" src="https://github.com/user-attachments/assets/d0612c04-9e9f-4133-9f30-0ca945211f83" />

Admin/Batch Request
       │
       ▼
┌─────────────────┐
│  Spring Boot    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│  Python Pricing │────▶│ Feature Engine  │
│     API         │     │ - 수요/공급      │
└────────┬────────┘     │ - 시즌/요일      │
         │              │ - 이벤트         │
         ▼              └─────────────────┘
┌─────────────────┐
│  ML Model       │
│  (XGBoost)      │
└────────┬────────┘
         │
         ▼
   추천 가격 반환

User Event
    │
    ▼
┌─────────────────┐
│  Spring Boot    │
│  (Producer)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│     Kafka       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌─────────────────┐
│  Python         │────▶│ Elasticsearch   │
│  (Consumer)     │     │                 │
└────────┬────────┘     └─────────────────┘
         │
         ▼
┌─────────────────┐
│  배치 집계       │
└────────┬────────┘
         │
         ▼
   Dashboard API

<img width="687" height="555" alt="image" src="https://github.com/user-attachments/assets/26dd77a1-a774-4304-8273-aa7e7b82616d" />

