from lib.models.magazine import Magazine

def test_magazine_save_and_find():
    mag = Magazine(name="Sumo", category="Wrestling")
    mag.save()

    assert mag.id is not None

    found = Magazine.find_by_id(mag.id)
    assert found.name == "Sumo"
    assert found.category == "Wrestling"
