from um import count

def test_nothing_but_um():
	assert count('um') == 1

def test_ums_in_mums():
	assert count('umm, mum can I, um, test these ums please') == 1

def test_umwords():
	assert count('Um, sum clumsy chum has an album of mums bum sounds') == 1