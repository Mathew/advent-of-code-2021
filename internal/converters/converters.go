package converters

import (
	"advent-of-code-2021/internal/structures"
	"github.com/pkg/errors"
"strconv"
	"strings"
)

func StringToInt(s string) (int, error) {
	r, err := strconv.Atoi(s)

	if err != nil {
		return 0, errors.WithMessagef(err, "Cannot convert to int: %s", s)
	}

	return r, nil
}

func StringsToInts(ss ...string) ([]int, error) {
	var is []int
	for _, s := range ss {
		r, err := StringToInt(s)
		if err != nil {
			return []int{}, err
		}

		is = append(is, r)
	}

	return is, nil
}

func BinaryToInt(ss ...string) (int64, error) {
	return strconv.ParseInt(strings.Join(ss, ""), 2, 64)
}

func TwoDimArrayFromString(s string, rowLength int) structures.TwoDimensionalStringArray {
	var ss structures.TwoDimensionalStringArray
	ss = append(ss, []string{})

	column := 0
	row := 0
	for _, c := range s {
		if column == rowLength {
			column = 0
			row += 1
			ss = append(ss, []string{})
		}
		ss[row] = append(ss[row], string(c))
		column += 1
	}

	return ss
}

