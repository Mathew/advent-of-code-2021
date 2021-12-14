package structures

func GetColumn(arr [][]string, column int) []string {
	var columnData []string
	for _, row := range arr {
		columnData = append(columnData, row[column])
	}

	return columnData
}

func Filter(arr [][]string, f func([]string) bool) [][]string {
	var filtered [][]string
	for _, r := range arr {
		if f(r) == true {
			filtered = append(filtered, r)
		}
	}

	return filtered
}

func Transpose(arr [][]string) [][]string {
	rows := len(arr)
	cols := len(arr[0])
	transposed := make([][]string, cols)
	for i := range transposed {
		transposed[i] = make([]string, rows)
	}

	for i := range arr {
		for j := range arr[i] {
			transposed[j][i] = arr[i][j]
		}
	}

	return transposed
}
