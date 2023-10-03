when (variable) {
    "foo" -> println("Foo!")
    "bar" -> {
        println("Baz!")
        println("Bar!")
    }
    else -> println("Fehler! Wert ist $variable")
}
