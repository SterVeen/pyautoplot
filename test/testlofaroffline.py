import unittest
import test.testcase as testcase
from pyautoplot.lofaroffline import *

class LofarOfflineTest(testcase.TestCase):

    def test_is_compute_node(self):
        self.assertTrue(is_compute_node('lce024'))
        self.assertFalse(is_compute_node('lce0241'))
        self.assertFalse(is_compute_node('lse024'))
        self.assertFalse(is_compute_node('lce02'))
        self.assertFalse(is_compute_node(''))
        pass


    def test_is_storage_node(self):
        self.assertTrue(is_storage_node('lse024'))
        self.assertFalse(is_storage_node('lse0241'))
        self.assertFalse(is_storage_node('lce024'))
        self.assertFalse(is_storage_node('lse02'))
        self.assertFalse(is_storage_node(''))
        pass


    def test_is_locus_node(self):
        self.assertTrue(is_locus_node('locus001'))
        self.assertTrue(is_locus_node('locus050'))
        self.assertTrue(is_locus_node('locus100'))        
        self.assertFalse(is_locus_node('lse0241'))
        self.assertFalse(is_locus_node('lce024'))
        self.assertFalse(is_locus_node('lhn001'))
        self.assertFalse(is_locus_node('lse02'))
        self.assertFalse(is_locus_node(''))


    def test_is_frontend_node(self):
        self.assertTrue(is_frontend_node('lfe001'))
        self.assertTrue(is_frontend_node('lhn001'))
        self.assertFalse(is_frontend_node('lfe0241'))
        self.assertFalse(is_frontend_node('lse024'))
        self.assertFalse(is_frontend_node('lfe02'))
        self.assertFalse(is_frontend_node(''))
        pass


    def test_get_node_number(self):
        self.assertEquals(get_node_number('lce012'), 12)
        pass


    def test_get_subcluster_number(self):
        self.assertEquals(get_subcluster_number('lce001'),1)
        self.assertEquals(get_subcluster_number('lce009'),1)
        self.assertEquals(get_subcluster_number('lce010'),2)
        self.assertEquals(get_subcluster_number('lce018'),2)
        self.assertEquals(get_subcluster_number('lce019'),3)
        self.assertEquals(get_subcluster_number('lce027'),3)

        self.assertEquals(get_subcluster_number('lse001'),1)
        self.assertEquals(get_subcluster_number('lse009'),3)
        self.assertEquals(get_subcluster_number('lse010'),4)
        self.assertEquals(get_subcluster_number('lse018'),6)
        self.assertEquals(get_subcluster_number('lse019'),7)

        self.assertRaises(ValueError, get_subcluster_number, 'lfe001')
        self.assertRaises(ValueError, get_subcluster_number, 'bgfen0')
        pass


    def test_get_node_number_in_subcluster(self):
        self.assertEquals(get_node_number_in_subcluster('lse004'), 0)
        self.assertEquals(get_node_number_in_subcluster('lce004'), 3)
        self.assertEquals(get_node_number_in_subcluster('lse009'), 2)
        self.assertEquals(get_node_number_in_subcluster('lce009'), 8)
        self.assertRaises(ValueError, get_node_number_in_subcluster, 'lfe001')
        pass


    def test_get_storage_node_names(self):
        [self.assertEquals(x,y) for x,y in zip(get_storage_node_names(1), ['lse001', 'lse002','lse003'])]
        [self.assertEquals(x,y) for x,y in zip(get_storage_node_names(2), ['lse004', 'lse005','lse006'])]
        [self.assertEquals(x,y) for x,y in zip(get_storage_node_names(3), ['lse007', 'lse008','lse009'])]
        [self.assertEquals(x,y) for x,y in zip(get_storage_node_names(4), ['lse010', 'lse011','lse012'])]
        pass


    def test_get_data_dirs(self):
        [self.assertEquals(found, expected) for found,expected in zip(get_data_dirs(1),
                                                                      ['/net/sub1/lse001/data1/',
                                                                       '/net/sub1/lse001/data2/',
                                                                       '/net/sub1/lse001/data3/',
                                                                       '/net/sub1/lse001/data4/',
                                                                       '/net/sub1/lse002/data1/',
                                                                       '/net/sub1/lse002/data2/',
                                                                       '/net/sub1/lse002/data3/',
                                                                       '/net/sub1/lse002/data4/',
                                                                       '/net/sub1/lse003/data1/',
                                                                       '/net/sub1/lse003/data2/',
                                                                       '/net/sub1/lse003/data3/',
                                                                       '/net/sub1/lse003/data4/'])]
        [self.assertEquals(found, expected) for found,expected in zip(get_data_dirs(3),
                                                                      ['/net/sub3/lse007/data1/',
                                                                       '/net/sub3/lse007/data2/',
                                                                       '/net/sub3/lse007/data3/',
                                                                       '/net/sub3/lse007/data4/',
                                                                       '/net/sub3/lse008/data1/',
                                                                       '/net/sub3/lse008/data2/',
                                                                       '/net/sub3/lse008/data3/',
                                                                       '/net/sub3/lse008/data4/',
                                                                       '/net/sub3/lse009/data1/',
                                                                       '/net/sub3/lse009/data2/',
                                                                       '/net/sub3/lse009/data3/',
                                                                       '/net/sub3/lse009/data4/'])]

        [self.assertEquals(found, expected) for found,expected in zip(get_data_dirs(3, root='testdata'),
                                                                      ['testdata/sub3/lse007/data1/',
                                                                       'testdata/sub3/lse007/data2/',
                                                                       'testdata/sub3/lse007/data3/',
                                                                       'testdata/sub3/lse007/data4/',
                                                                       'testdata/sub3/lse008/data1/',
                                                                       'testdata/sub3/lse008/data2/',
                                                                       'testdata/sub3/lse008/data3/',
                                                                       'testdata/sub3/lse008/data4/',
                                                                       'testdata/sub3/lse009/data1/',
                                                                       'testdata/sub3/lse009/data2/',
                                                                       'testdata/sub3/lse009/data3/',
                                                                       'testdata/sub3/lse009/data4/'])]
        pass


    def test_find_msses(self):
        self.assertEquals(len(find_msses('L2010_98765', root='testdata/net', node_name='lce040')), 0)

        msses = sorted(find_msses('L2010_12345', root='testdata/net', node_name='lce030'))
        expected = ['testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB117-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB118-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB119-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB120-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB121-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB122-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB123-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB124-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB125-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB126-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB127-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB128-uv.MS',
                    'testdata/net/sub4/lse010/data1/L2010_12345/L12345_SB129-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB130-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB131-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB132-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB133-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB134-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB135-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB136-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB137-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB138-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB139-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB140-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB141-uv.MS',
                    'testdata/net/sub4/lse012/data1/L2010_12345/L12345_SB142-uv.MS']
        self.assertEquals(len(msses), len(expected))
        for m,e in zip(msses,expected):
            self.assertEquals(m,e)
            pass
        pass




if __name__ == '__main__':
    unittest.main()
    pass
