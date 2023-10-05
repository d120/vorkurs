fun kreisFlaeche(r: Double) = r * r * Math.PI

// Volumen eines Zylinders berechnen
fun zylinderVol(r: Double, h: Double) = kreisFlaeche(r) * h
// Oberfläche einer Kugel berechen
fun kugelOberflaeche(r: Double) = 4 * kreisFlaeche(r)
// Oberfläche einer Halbkugel berechnen
fun hemisphereOberflaeche(r: Double) =
    kugelOberflaeche(r) / 2 + kreisFlaeche(r)
