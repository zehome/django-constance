from django.db.models import signals


def create_perm(app, created_models, verbosity, db, **kwargs):
    """
    Creates a fake content type and permission
    to be able to check for permissions
    """
    from django import VERSION
    from django.contrib.auth.models import Permission
    from django.contrib.contenttypes.models import ContentType

    if VERSION >= (1, 8):
        content_type, created = ContentType.objects.get_or_create(
            app_label='constance',
            model='config')
    else:
        content_type, created = ContentType.objects.get_or_create(
            name='config',
            app_label='constance',
            model='config')

    permission, created = Permission.objects.get_or_create(
        name='Can change config',
        content_type=content_type,
        codename='change_config')


signals.post_syncdb.connect(create_perm, dispatch_uid="constance.create_perm")
