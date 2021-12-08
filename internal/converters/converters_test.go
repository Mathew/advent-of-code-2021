package converters

import (
	"advent-of-code-2021/internal/structures"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestTwoDimArrayfromString(t *testing.T) {
	assert.Equal(t,
		structures.TwoDimensionalStringArray{
			{"a", "b", "c"},
			{"d", "e", "f"},
		},
		TwoDimArrayFromString("abcdef", 3),
	)
	assert.Equal(t,
		structures.TwoDimensionalStringArray{
			{"f", "e", "d"},
			{"c", "a", "b"},
		},
		TwoDimArrayFromString("fedcab", 3),
	)
}
