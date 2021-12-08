package structures

type TwoDimensionalStringArray [][]string

func (arr TwoDimensionalStringArray) GetColumn(column int) []string {
	var columnData []string
	for _, row := range arr {
		columnData = append(columnData, row[column])
	}

	return columnData
}

func (arr TwoDimensionalStringArray) Filter(f func([]string)bool) TwoDimensionalStringArray {
	filtered := TwoDimensionalStringArray{}
	for _, r := range arr {
		if f(r) == true {
			filtered = append(filtered, r)
		}
	}

	return filtered
}
