package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestCountBoolIf(t *testing.T) {
	counter := CountBoolIf(true)
	assert.Equal(t, 1, counter(true))
	assert.Equal(t, 2, counter(true))
	assert.Equal(t, 2, counter(false))
	assert.Equal(t, 3, counter(true))
}
