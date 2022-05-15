from pathlib import Path
from unittest import TestCase

import bulrush


class ExportTest(TestCase):

    def test_environment(self):
        extensions = bulrush.ENVIRONMENT.get('extensions', [])
        self.assertIn('webassets.ext.jinja2.AssetsExtension', extensions)

    def test_filters(self):
        self.assertIn('images', bulrush.FILTERS)
        self.assertIs(bulrush.FILTERS['images'], bulrush.extract_images)
        self.assertIn('license', bulrush.FILTERS)
        self.assertIs(bulrush.FILTERS['license'], bulrush.generate_license)
        self.assertIn('schema', bulrush.FILTERS)
        self.assertIs(bulrush.FILTERS['schema'], bulrush.generate_jsonld_schema)

    def test_path(self):
        expected = str(Path(__file__).parent.parent.joinpath('bulrush'))
        self.assertEqual(bulrush.PATH, expected)
