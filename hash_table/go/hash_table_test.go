package hashtable

import (
	"testing"
	"testing/quick"
)

func TestDoesntLoseData(t *testing.T) {
	checker := func(ln int) func([]byte, string) bool {
		h := NewHashTable(ln)

		return func(key []byte, value string) bool {
			h.Set(key, value)

			recovered, ok := h.Get(key).(string)

			return ok && value == recovered
		}
	}

	for _, length := range []int{1, 2, 10, 300, 1000, 10000, 1000000} {
		if err := quick.Check(checker(length), nil); err != nil {
			t.Error(err)
		}
	}
}
