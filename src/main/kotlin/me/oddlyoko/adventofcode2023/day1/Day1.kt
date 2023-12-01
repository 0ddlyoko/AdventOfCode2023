package me.oddlyoko.adventofcode2023.day1

fun main() {
    Day1()
}

class Day1 {
    private val NUMBERS = arrayOf("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

    init {
        // Code is ugly, and I don't care :D
        // Part 1
        val data = readFile()
        var total = 0
        data.forEach { word ->
            var firstDigit = -1
            var lastDigit = -1
            word.forEach { c ->
                if (c in '0'..'9') {
                    if (firstDigit == -1)
                        firstDigit = c - '0'
                    lastDigit = c - '0'
                }
            }
            var sum = firstDigit
            if (lastDigit != -1) {
                sum *= 10
                sum += lastDigit
            }
            total += sum
        }
        println("Part 1: $total")

        // Part 2
        total = 0
        data.forEach { word ->
            var firstDigit = -1
            var lastDigit = -1
            word.forEachIndexed { i, char ->
                if (char in '0'..'9') {
                    if (firstDigit == -1)
                        firstDigit = char - '0'
                    lastDigit = char - '0'
                }
                NUMBERS.forEachIndexed { numberIdx, number ->
                    if (char == number[0]) {
                        // Check if it's this number
                        if (word.length >= i + number.length && word.substring(i, i + number.length) == number) {
                            if (firstDigit == -1)
                                firstDigit = numberIdx + 1
                            lastDigit = numberIdx + 1
                        }
                    }
                }
            }
            var sum = firstDigit
            if (lastDigit != -1) {
                sum *= 10
                sum += lastDigit
            }
            total += sum
        }
        println("Part 2: $total")
    }

    private fun readFile(): List<String> =
        this::class.java.getResourceAsStream("day1.txt")?.bufferedReader()?.readLines() ?: listOf()
}
