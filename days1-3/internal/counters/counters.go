package counters

import "sort"

type StringCounter struct {
	Counts map[string]int
}

func NewStringCounter () StringCounter {
	return StringCounter{Counts: map[string]int{}}
}

func (sc *StringCounter) Count (ss... string) {
	for _, s := range ss {
		sc.Counts[s] += 1
	}
}

func (sc *StringCounter) Sorted() []string {
	var keys []string
	for name := range sc.Counts {
		keys = append(keys, name)
	}
	sort.Slice(keys, func(i, j int) bool {
		return sc.Counts[keys[i]] > sc.Counts[keys[j]]
	})

	return keys
}

func Filter(match string, items... string) []string {
	var matches []string
	for _, i := range items {

		if i == match {
			matches = append(matches, match)
		}
	}

	return matches
}