import pytest

@pytest.fixture
def context(browser, request):
    ctx = browser.new_context()
    ctx.tracing.start(screenshots=True, snapshots=True, sources=True)
    yield ctx
    ctx.tracing.stop(path=f"test-results/{request.node.name}/trace.zip")
    ctx.close()