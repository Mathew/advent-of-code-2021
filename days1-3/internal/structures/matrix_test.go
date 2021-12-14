package structures

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestGetColumn(t *testing.T) {
	twoDim := [][]string{
		{"a", "1", "One"},
		{"b", "2", "Two"},
		{"c", "3", "Three"},
	}

	assert.Equal(t, []string{"a", "b", "c"}, GetColumn(twoDim, 0))
}

func TestFilter(t *testing.T) {
	twoDim := [][]string{
		{"a", "1", "One"},
		{"b", "2", "Two"},
		{"c", "3", "Three"},
	}

	arr := Filter(twoDim, func(strings []string) bool {
		return strings[1] == "2"
	})

	assert.Equal(t, [][]string{{"b", "2", "Two"}}, arr)
}

func TestTranspose(t *testing.T) {
	input := [][]string{
		{"1", "2", "3"},
		{"4", "5", "6"},
	}

	exp := [][]string{
		{"1", "4"},
		{"2", "5"},
		{"3", "6"},
	}

	assert.Equal(t, exp, Transpose(input))
}
