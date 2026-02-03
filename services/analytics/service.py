from typing import List, Dict, Optional
from datetime import datetime, timedelta
import random

class AnalyticsService:
    def __init__(self):
        pass
    async def get_analytics(
            self,
            user_id: Optional[str] = None,
            start_date: Optional[datetime] = None,
            end_date: Optional[datetime] = None,
            metrics: List[str] = None
    ) -> dict:
        """분석 데이터 조회"""
        if not metrics:
            metrics = ["views", "clicks", "conversions"]
        if not start_date:
            start_date = datetime.utcnow() - timedelta(days=30)
        if not end_date:
            end_date = datetime.utcnow()
        # TODO: 실제 DB에서 데이터 조회
        metrics_data = await self._calculate_metrics(
            user_id, start_date, end_date, metrics
        )
        trends = await self._calculate_trends(
            start_date, end_date, metrics
        )
        return {
            "period": {
                "start": start_date,
                "end": end_date
            },
            "metrics": metrics_data,
            "trends": trends,
            "generated_at": datetime.utcnow()
        }
    async def _calculate_metrics(
            self,
            user_id: Optional[str],
            start_date: datetime,
            end_date: datetime,
            metrics: List[str]
    ) -> Dict[str, float]:
        """메트릭 계산 (TODO: 실제 데이터 연동)"""
        # 임시 데이터 생성
        result = {}
        if "views" in metrics:
            result["views"] = random.randint(1000, 10000)
        if "clicks" in metrics:
            result["clicks"] = random.randint(100, 1000)
        if "conversions" in metrics:
            result["conversions"] = random.randint(10, 100)
        if "revenue" in metrics:
            result["revenue"] = round(random.uniform(10000, 100000), 2)
        # CTR, CVR 계산
        if "views" in result and "clicks" in result:
            result["ctr"] = round(result["clicks"] / result["views"] * 100, 2)
        if "clicks" in result and "conversions" in result:
            result["cvr"] = round(result["conversions"] / result["clicks"] * 100, 2)
        return result
    async def _calculate_trends(
            self,
            start_date: datetime,
            end_date: datetime,
            metrics: List[str]
    ) -> List[Dict]:
        """트렌드 데이터 계산"""
        trends = []
        days = (end_date - start_date).days
        for i in range(min(days, 7)):  # 최근 7일
            date = end_date - timedelta(days=i)
            trend_item = {
                "date": date.strftime("%Y-%m-%d"),
                "views": random.randint(100, 1000),
                "clicks": random.randint(10, 100),
                "conversions": random.randint(1, 10)
            }
            trends.append(trend_item)
        return list(reversed(trends))
# 싱글톤 인스턴스
analytics_service = AnalyticsService()
