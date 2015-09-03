package heap

import (
	"reflect"
	"testing"
)

func TestFunctionsCorrectly(t *testing.T) {
	h := NewHeap()
	input := 1

	h.Insert(input)

	assert(t, h.Remove(), input)
}

func TestAlwaysKeepsMinimumAtSpotZero(t *testing.T) {
	h := NewHeap()
	max := 20000

	for i := max; i > 0; i-- {
		h.Insert(i)
	}

	for i := 1; i <= max; i++ {
		assert(t, h.data[0], i)
		assert(t, h.Peek(), i)

		assert(t, h.Remove(), i)
	}
}

func assert(t *testing.T, left, right interface{}) {
	if !reflect.DeepEqual(left, right) {
		t.Errorf("expected %v to == %v", left, right)
	}
}
