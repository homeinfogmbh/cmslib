"""Hooks for filedb actions."""

from cmslib.config import LOGGER as _LOGGER
from cmslib.orm.charts import blackboard, image_text, weather
from cmslib.orm.charts.video import Video
from cmslib.orm.configuration import Configuration


__all__ = ['on_delete']


LOGGER = _LOGGER.getChild('file_hooks')


def _remove_bc_images(ident):
    """Removes the respective images of Blackboard charts."""

    for image in blackboard.Image.select().where(
            blackboard.Image.image == ident):
        LOGGER.info(
            'Deleting blackboard.Image %i with image %i.',
            image.id, ident)
        image.delete_instance()


def _remove_itc_images(ident):
    """Removes the respective images of ImageText charts."""

    for image in image_text.Image.select().where(
            image_text.Image.image == ident):
        LOGGER.info(
            'Deleting image_text.Image %i with image %i.', image.id, ident)
        image.delete_instance()


def _remove_wc_image(ident):
    """Removes the respective images of Weather charts."""

    for image in weather.Image.select().where(weather.Image.image == ident):
        LOGGER.info(
            'Deleting weather.Image %i with image %i.', image.id, ident)
        image.delete_instance()


def _null_video_charts(ident):
    """Sets the image fields of the
    respective video charts to NULL.
    """

    for video in Video.select().where(Video.video == ident):
        LOGGER.info('Setting video = %i to NULL on Video %i.', ident, video.id)
        video.video = None
        video.save()


def _null_configurations(ident):
    """Sets the image fields of the
    respective configurations to NULL.
    """

    for configuration in Configuration.select().where(
            (Configuration.logo == ident)
            | (Configuration.background == ident)
            | (Configuration.dummy_picture == ident)):
        if configuration.logo == ident:
            LOGGER.info(
                'Setting logo = %i to NULL on Configuration %i.',
                ident, configuration.id)
            configuration.logo = None

        if configuration.background == ident:
            LOGGER.info(
                'Setting background = %i to NULL on Configuration %i.',
                ident, configuration.id)
            configuration.background = None

        if configuration.dummy_picture == ident:
            LOGGER.info(
                'Setting dummy_picture = %i to NULL on Configuration %i.',
                ident, configuration.id)
            configuration.dummy_picture = None

        configuration.save()


def on_delete(ident):
    """Runs when the file with the respective ID has been deleted."""

    _remove_bc_images(ident)
    _remove_itc_images(ident)
    _remove_wc_image(ident)
    _null_video_charts(ident)
    _null_configurations(ident)
