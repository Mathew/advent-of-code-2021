package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestHigherOrLower(t *testing.T) {
	assert.Equal(t, true, HigherOrLower(1, 2))
	assert.Equal(t, false, HigherOrLower(2, 1))
}

func TestCountBoolIf(t *testing.T) {
	counter := CountBoolIf(true)
	assert.Equal(t, 1, counter(true))
	assert.Equal(t, 2, counter(true))
	assert.Equal(t, 2, counter(false))
	assert.Equal(t, 3, counter(true))
}
