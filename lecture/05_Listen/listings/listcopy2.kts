val myList = mutableListOf(5, 7, 8, 42)
val kopie = myList.toMutableList() // kopiert alle Werte

println(myList[0])  // 5
println(myList[1])  // 7

kopie[1] = 2
println(myList[1])  // 7
println(kopie[1])  // 2
