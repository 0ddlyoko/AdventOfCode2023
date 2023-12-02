package me.oddlyoko.adventofcode2023.day2

fun main() {
    Day2()
}

class Day2 {
    val COLORS = mapOf(
        "red" to 12,
        "green" to 13,
        "blue" to 14,
    )
    val COLORS_IDX = arrayOf("red", "green", "blue")

    init {
        // Code is ugly, and I don't care :D
        val data = readFile()
        var total = 0
        var total2 = 0
        data.forEach { word ->
            val split = word.split(": ")
            val gameId = split[0].substring(5).toInt()
            val cubeSets = split[1].split("; ")
            var shouldWeTake = true
            val max = mutableListOf(0, 0, 0)
            cubeSets.forEach { cubes ->
                cubes.split(", ").forEach {
                    val a = it.split(" ")
                    val number = a[0].toInt()
                    val type = a[1]
                    if (number > COLORS[type]!!)
                        shouldWeTake = false
                    if (max[COLORS_IDX.indexOf(type)] < number)
                        max[COLORS_IDX.indexOf(type)] = number
                }
            }
            if (shouldWeTake) {
                total += gameId
            }
            total2 += max[0] * max[1] * max[2]
        }
        println("Part 1: $total")
        println("Part 2: $total2")
    }

    private fun readFile(): List<String> =
        this::class.java.getResourceAsStream("day2.txt")?.bufferedReader()?.readLines() ?: listOf()
}
