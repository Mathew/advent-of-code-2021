package main

import (
	"advent-of-code-2021/internal/converters"
	"advent-of-code-2021/internal/files"
	"advent-of-code-2021/internal/structures"
	"log"
	"strings"
)

func CallBall(balls []int) func() int {
	ptr := -1
	return func() int {
		ptr += 1
		return balls[ptr]
	}
}

type BingoCard struct {
	rows      [][]int
	cols      [][]int
	marked    []int
	itsABingo bool
}

func NewBingoCard(balls [][]string) (BingoCard, error) {
	return BingoCard{
		rows:      balls,
		cols:      structures.Transpose(balls),
		marked:    nil,
		itsABingo: false,
	}, nil
}

func main() {
	var err error

	defer func() {
		if err != nil {
			log.Fatalf("%+v", err)
		}
	}()

	rawBingo, err := files.Load("cmd/day4/input.txt", "\n")
	if err != nil {
		return
	}

	calls, err := converters.StringsToInts(strings.Split(rawBingo[0], ",")...)
	if err != nil {
		return
	}

	baller := CallBall(calls)
	var cards []BingoCard

	for i := 1; i < len(rawBingo[1:]); i += 5 {
		cards = append(cards, NewBingoCard(converters.MatrixFromString(strings.Join(rawBingo[i:i+5], ""), 5)))
	}

	BingoCards := NewBingoCards()
	Bingo := NewBingo(BingoCaller, BingoCards)

	Bingo.Start()
}
