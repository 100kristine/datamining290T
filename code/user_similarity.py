from mrjob.job import MRJob
from mrjob.protocol import JSONValueProtocol

class UserSimilarity(MRJob):
    INPUT_PROTOCOL = JSONValueProtocol

    ###
    # TODO: write the functions needed to
    # 1) find potential matches,
    # 2) calculate the Jaccard between users, with a user defined as a set of
    # reviewed businesses
    ##/

    #Jaccard index = len(intersection)/len(union)
    def getRecord(self, _,record):
        """Mapper: Takes in review entry and emits pairs of user ids and business ids"""
        if record['type']=='review':
            yield [record['user_id'],record['business_id']]

    def outputUserReviews(self, user_id,business_ids): 
        """Reducer: Collects business ids by user"""
        businesses = list(business_ids)
        yield [user_id,businesses]

    def aggregate(self,user_id,business_ids):
        """Reducer"""
        yield ["Distance",[user_id,business_ids]]
    
    def getPairs(self,stat,info):
        for item in info:
            for otherItem in info:
               yield [[item[0],otherItem[0]],[item[1],otherItem[1]]]

    def returnDistance(self,pair,businessInfo):
        """Reducer:"""
        #print info[0]
        def getIntersection(lst,otherlst):
            intersection = []
            for i in lst:
                if i in otherlst:
                    intersection +=[i]
            return intersection
        def distance(item,otherItem):
            #distance = intersection/union
            intersect = len(getIntersection(item,otherItem))
            union = float(len(set(item+otherItem)))
            return intersect/union
        pairs = []
        if pair in pairs or [pair[1],pair[0]] in pairs:
            pass
        else:
            pairs += [pair]
            dist = distance(businessInfo[0],businessInfo[1])
            if dist >= 0.5:
                yield [pair,dist]


    def steps(self):
        """TODO: Document what you expect each mapper and reducer to produce:
        mapper1: <line, record> => <key, value>
        reducer1: <key, [values]>
        mapper2: ...
        """
        return [
            self.mr(mapper=self.getRecord, reducer=self.outputUserReviews),
                    self.mr(mapper=self.aggregate,reducer=self.getPairs),
                    self.mr(mapper=self.returnDistance)
                    ]


if __name__ == '__main__':
    UserSimilarity.run()
