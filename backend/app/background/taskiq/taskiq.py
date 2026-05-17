import ssl

from taskiq_redis import ListQueueBroker, RedisAsyncResultBackend  # type: ignore[import]

from app.config import settings

redis_kwargs = {}

if settings.REDIS_URL.startswith("rediss://"):
    _ssl_ctx = ssl.create_default_context()

    _ssl_ctx.check_hostname = False
    _ssl_ctx.verify_mode = ssl.CERT_NONE

    redis_kwargs["ssl"] = _ssl_ctx

broker = ListQueueBroker(
    url=settings.REDIS_URL,
    redis_kwargs=redis_kwargs,
).with_result_backend(
    RedisAsyncResultBackend(
        redis_url=settings.REDIS_URL,
        redis_kwargs=redis_kwargs,
    )
)