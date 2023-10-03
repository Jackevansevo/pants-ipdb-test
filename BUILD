python_requirements(
    name="reqs0",
)

python_sources(
    name="root",
)

pex_binary(
    name="flask",
    entry_point="flask",
    args=["run"],
    dependencies=["//:reqs0#python-dotenv"]
)

pex_binary(
    name="gunicorn",
    entry_point="gunicorn",
    args=["main:create_app()"],
    dependencies=["//:root"]
)

python_tests(
    name="tests0",
)
