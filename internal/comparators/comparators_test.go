package comparators

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestIsHigherNumber(t *testing.T) {
	assert.Equal(t, true, IsHigherNumber(1, 2))
	assert.Equal(t, false, IsHigherNumber(2, 1))
	assert.Equal(t, false, IsHigherNumber(1, 1))
}
