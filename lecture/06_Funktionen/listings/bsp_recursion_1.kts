fun fib(x: Int): Int {
    if (x <= 1) {
        return 1
    }
    return fib(x - 1) + fib(x - 2)
}

