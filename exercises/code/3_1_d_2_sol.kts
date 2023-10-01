print("Gebe eine Zahl ein: ")
val prime = readln().toInt()

var isPrime = true
if (prime <= 1) {
    isPrime = false
} else {
    for (i in 2 until prime) {
        if (prime % i == 0) {
            isPrime = false
            break
        }
    }
}

if (isPrime) {
    println("$prime ist eine Primzahl.")
} else {
    println("$prime ist keine Primzahl.")
}
