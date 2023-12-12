import pytest
from app.core.application import Application
from app.core.autoscaler import AutoScaler 

async def mock_get_current_status_high():
    return {"cpu": {"highPriority": 0.85}, "replicas": 5}

async def mock_get_current_status_low():
    return {"cpu": {"highPriority": 0.75}, "replicas": 5}

@pytest.mark.asyncio
async def test_scaling_up():
    app = Application()
    scaler = AutoScaler(app, target_cpu_usage=0.80)
    app.get_current_status = mock_get_current_status_high
    assert await scaler.scale() == 6

@pytest.mark.asyncio
async def test_scaling_down():
    app = Application()
    scaler = AutoScaler(app, target_cpu_usage=0.80)
    app.get_current_status = mock_get_current_status_low
    assert await scaler.scale() == 4
