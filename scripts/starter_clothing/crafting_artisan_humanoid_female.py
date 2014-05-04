import sys

def CraftingArtisanHumanoidFemale(core, object):
	dress = core.objectService.createObject('object/tangible/wearables/dress/shared_dress_s29.iff', object.getPlanet())
	necklace = core.objectService.createObject('object/tangible/wearables/necklace/shared_necklace_s02.iff', object.getPlanet())
	bracelet_l = core.objectService.createObject('object/tangible/wearables/bracelet/shared_bracelet_s03_l.iff', object.getPlanet())
	bracelet_r = core.objectService.createObject('object/tangible/wearables/bracelet/shared_bracelet_s03_r.iff', object.getPlanet())
	bracelet_l_2 = core.objectService.createObject('object/tangible/wearables/bracelet/shared_bracelet_s06_l.iff', object.getPlanet())
	bracelet_r_2 = core.objectService.createObject('object/tangible/wearables/bracelet/shared_bracelet_s06_r.iff', object.getPlanet())
	shoes = core.objectService.createObject('object/tangible/wearables/shoes/shared_shoes_s07.iff', object.getPlanet())
	inventory = object.getSlottedObject('inventory')
	inventory.add(bracelet_l_2)
	inventory.add(bracelet_r_2)
	object._add(dress)
	object._add(necklace)
	object._add(bracelet_l)
	object._add(bracelet_r)
	object._add(shoes)
