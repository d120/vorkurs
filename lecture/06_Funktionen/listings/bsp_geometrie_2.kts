fun kreisFlaeche(r: Double): Double {
    return r * r * Math.PI
}

// Hauptprogramm
val radius = 20.5
println(
    "Der Flächeninhalt eines Kreises mit Radius $radius" +
        " cm ist ${kreisFlaeche(radius)} cm^2"
)
