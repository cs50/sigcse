import check50
import check50.c

@check50.check()
def compiles():
    """hello compiles"""
    check50.c.compile("hello.c")

@check50.check(compiles)
def prints_hello():
    """prints exactly hello world"""
    check50.run("./hello").stdout("hello world").exit(0)
