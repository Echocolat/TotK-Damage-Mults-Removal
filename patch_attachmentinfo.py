import byml
import math

def patch(version):

    with open(f'SpearTwoHandedMultRemoval/romfs/RSDB/AttachmentActorInfo.Product.{version}.rstbl.byml', 'rb') as aai_file:
        aai_parser = byml.Byml(aai_file.read())
        aai_data = aai_parser.parse()

    for aai_dict in aai_data:
        if aai_dict['__RowId'].startswith('Weapon_Lsword_'):
            if 'AttachmentAdditionalDamage' in aai_dict:
                aai_dict['AttachmentAdditionalDamage'] = byml.Int(math.floor(aai_dict['AttachmentAdditionalDamage'] / 0.95 + 1))
            if 'AttachmentShieldBashDamage' in aai_dict:
                aai_dict['AttachmentShieldBashDamage'] = byml.Int(aai_dict['AttachmentAdditionalDamage'])
        elif aai_dict['__RowId'].startswith('Weapon_Spear_'):
            if 'AttachmentAdditionalDamage' in aai_dict:
                aai_dict['AttachmentAdditionalDamage'] = byml.Int(math.ceil(aai_dict['AttachmentAdditionalDamage'] / 1.326856 - 1))
            if 'AttachmentShieldBashDamage' in aai_dict:
                aai_dict['AttachmentShieldBashDamage'] = byml.Int(aai_dict['AttachmentAdditionalDamage'])

    writer = byml.Writer(aai_data, be = False, version = 7)
    with open(f'SpearTwoHandedMultRemoval/romfs/RSDB/AttachmentActorInfo.Product.{version}.rstbl.byml', 'wb') as aai_file:
        writer.write(aai_file)

def patch_all():

    for version in ['100', '110', '111', '112', '120', '121']:
        patch(version)

patch_all()