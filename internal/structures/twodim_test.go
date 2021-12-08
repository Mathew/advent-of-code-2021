package structures

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestTwoDimensionalStringArray_GetColumn(t *testing.T) {
	twoDim := TwoDimensionalStringArray{
		[]string{"a", "1", "One"},
		[]string{"b", "2", "Two"},
		[]string{"c", "3", "Three"},
	}

	assert.Equal(t, []string{"a", "b", "c"}, twoDim.GetColumn(0))
}

func TestTwoDimensionalStringArray_Filter(t *testing.T) {
	twoDim := TwoDimensionalStringArray{
		[]string{"a", "1", "One"},
		[]string{"b", "2", "Two"},
		[]string{"c", "3", "Three"},
	}

	arr := twoDim.Filter(func(strings []string) bool {
		return strings[1] == "2"
	})

	assert.Equal(t, TwoDimensionalStringArray{{"b", "2", "Two"}}, arr)
}
