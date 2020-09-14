import sys
sys.path.append('..')

from main_multi import ImageSimilarity, DeepModel

class NewImageSimilarity(ImageSimilarity):
    @staticmethod
    def _sub_process(para):
        # Override the method from the base class
        path, fields = para['path'], para['fields']
        try:
            feature = DeepModel.preprocess_image(path)
            return feature, fields

        except Exception as e:
            print('Error file %s: %s' % (fields[0], e))

        return None, None


if __name__ == "__main__":
    similarity = NewImageSimilarity()

    '''Setup'''
    similarity.batch_size = 16
    similarity.num_processes = 2

    '''Load source data'''
    #test1 = similarity.load_data_csv('./test1.csv', delimiter=',')
    #test2 = similarity.load_data_csv('./test2.csv', delimiter=',', cols=['id', 'path'])

    test1 = similarity.load_data_csv('./demo_custom_test1.csv', delimiter=',')
    test2 = similarity.load_data_csv('./demo_custom_test2.csv', delimiter=',', cols=['id', 'path'])


    '''Save features and fields'''
    similarity.save_data('test1', test1)
    similarity.save_data('test2', test2)

    
    '''Calculate similarities'''
    #result = similarity.iteration(['test1_id', 'test1_url', 'test2_id', 'test2_url'], thresh=0.845)
    result = similarity.iteration(['test1_id', 'test1_url', 'test2_id', 'test2_url'], thresh=0.5)
    print('Row for source file 1, and column for source file 2.')
    print(result)
