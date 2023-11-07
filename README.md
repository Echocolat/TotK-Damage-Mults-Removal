## Spear and two handed multipliers removal for Tears of the Kingdom

#### Explanations 

In vanilla Tears of the Kingdom, spears and two handed weapons do not show the same damage as what they actually do. Unfused / no modified spears show `ceil(true_damage * 1.326856)` damage, unfused / no modified two handed weapons show `floor(true_damage * 0.95)` damage. These multipliers also affect fuse, modifier and zonaite-powered damage. To calculate spear additional damage, the game does `true_add_damage = ceil( (fuse_damage + modifier_damage + zonaite_damage) * 0.7536613)`, and for two handed weapons it does `true_add_damage = floor( (fuse_damage + modifier_damage + zonaite_damage) * 1.052632)`.

This mod aims to completely remove these multipliers from the game period.

#### How to install

Make sure your console/emulator is able to use IPS patches. Then, just drag down the mod pack inside your mod folder.

#### Compatibility issues

This mod edits RSDB/AttachmentActorInfo.Product.XXX files, as well as all spear / two handed weapon actor packs in order to restore the damage Two handed weapons and Spears deal when used as fuse materials. 

#### Credits

Huge thanks to dt12345, Doge228, phil_macrocheira for the months of support and help researching on these multipliers.