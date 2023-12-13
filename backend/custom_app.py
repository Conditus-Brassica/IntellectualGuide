import typing as t

from flask import Flask

from backend.broker.abstract_agents_broker import AbstractAgentsBroker


class CustomApp(Flask):
    def run(
            self,
            broker: AbstractAgentsBroker,
            host: str | None = None,
            port: int | None = None,
            debug: bool | None = None,
            load_dotenv: bool = True,
            **options: t.Any,
    ) -> None:
        broker.startup()
        super().run(host, port, debug, load_dotenv, **options)
        broker.shutdown()
