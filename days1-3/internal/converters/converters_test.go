package converters

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestMatrixFromString(t *testing.T) {
	assert.Equal(t,
		[][]string{
			{"a", "b", "c"},
			{"d", "e", "f"},
		},
		MatrixFromString("abcdef", 3),
	)
	assert.Equal(t,
		[][]string{
			{"f", "e", "d"},
			{"c", "a", "b"},
		},
		MatrixFromString("fedcab", 3),
	)
}
