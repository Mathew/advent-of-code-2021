package counters

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestStringCounter(t *testing.T) {
	sc := NewStringCounter()
	sc.Count("b")
	sc.Count("c")
	sc.Count("a")
	sc.Count("a")
	sc.Count("a")
	sc.Count("b")
	assert.Equal(t, []string{"a", "b", "c"}, sc.Sorted())
}
