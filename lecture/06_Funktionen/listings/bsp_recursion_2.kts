fun fib(x: Int): Int {
    if (x <= 1) { // Rekursionsanker
        return 1
    }
    // Rekursionsaufruf
    return fib(x - 1) + fib(x - 2)
}

