package me.oddlyoko.adventofcode2023.day3

fun main() {
    Day3()
}

class Day3 {
    init {
        // Code is ugly, and I don't care :D
        val data = readFile()
        val width = data[0].length
        val mapForPart2 = mutableMapOf<Int, MutableList<Int>>()
        var total = 0
        data.forEachIndexed { i, line ->
            var number = 0
            var hasSymbol = false
            var posX = -1
            line.forEachIndexed { j, c ->
                if (c in '0'..'9') {
                    number *= 10
                    number += c - '0'
                    // Check around if there is symbols somewhere
                    for (i2 in i - 1..i + 1) {
                        if (i2 < 0 || i2 >= data.size)
                            continue
                        for (j2 in j - 1 .. j + 1) {
                            if (j2 < 0 || j2 >= line.length)
                                continue
                            val symb = data[i2][j2]
                            if ((symb < '0' || symb > '9') && symb != '.')
                                hasSymbol = true
                            if (symb == '*')
                                posX = j2 * width + i2
                        }
                    }
                } else {
                    if (hasSymbol)
                        total += number
                    hasSymbol = false
                    if (posX != -1)
                        mapForPart2.getOrPut(posX) { mutableListOf() }.add(number)
                    posX = -1
                    number = 0
                }
            }
            if (hasSymbol)
                total += number
            if (posX != -1)
                mapForPart2.getOrPut(posX) { mutableListOf() }.add(number)
        }
        println("Part 1: $total")
        val part2 = mapForPart2.values.filter { it.size > 1 }.map { it.reduce { acc, i -> acc * i } }.sum()
        println("Part 2: $part2")
    }

    private fun readFile(): List<String> =
        this::class.java.getResourceAsStream("day3.txt")?.bufferedReader()?.readLines() ?: listOf()
}
