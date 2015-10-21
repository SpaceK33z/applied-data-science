# Assignment 1

Starting mongodb with `mongod --config /usr/local/etc/mongod.conf` in a screen session. Then import db: `mongoimport --db scratch --collection zips --file zips.json`.

3. Exploring data:

```
mongo
> show dbs
> use scratch
> show collections
> db.zips.find()
```

4. Indexes:

```
> db.zips.find().count()
29353
> db.zips.find({"city":"FLAGSTAFF"}).count()
2
> db.zips.find({"city":"FLAGSTAFF"}).explain("executionStats")
```

I then added the index using:

```
> db.zips.createIndex({city: 1})
{
    "createdCollectionAutomatically" : false,
    "numIndexesBefore" : 1,
    "numIndexesAfter" : 2,
    "ok" : 1
}
> db.zips.find({"city":"FLAGSTAFF"}).explain("executionStats")
```

After adding this index, it will use the index when querying the zips collection for a city.
In the explain query, `executionStages` has an `indexName` that is called `city_1`. This means that the index is used for this query.

5. Queries

a.

```
> db.zips.find().count()
29353
```

b.

```
> db.zips.find({"state": "MA"}).count()
474
```

c.

```
> db.zips.distinct("state")
[
    "MA",
    "RI",
    ...
]
```

d.

```
> db.zips.distinct("state").sort({state: 1})
[
    "AK",
    "AL",
    ...
]
```

e.

```
> db.zips.distinct("state").length
51
```

f.

```
> db.zips.find({pop: {$lt: 50}}).count()
356
```


g.

```
> db.zips.distinct("city", {pop: {$lt: 50}})
[
    "BUCKLAND",
    "CAMBRIDGE",
    "CLAYVILLE",
    ...
}
```

6. GeoNear index

a.

```
> db.zips.createIndex({"loc": "2dsphere"})
{
    "createdCollectionAutomatically" : false,
    "numIndexesBefore" : 2,
    "numIndexesAfter" : 3,
    "ok" : 1
}
```

b. Find locations within 5000 meters from Flagstaff

Searched latitude and longitude of Flagstaff using http://www.latlong.net/.

```
> db.zips.find({
    loc: { $near: {
        $geometry: { type: "Point",  coordinates: [ -111.651302, 35.198284 ] },
        $maxDistance: 5000
    } }
})

{ "_id" : "86001", "city" : "FLAGSTAFF", "loc" : [ -111.661979, 35.185911 ], "pop" : 30174, "state" : "AZ" }
```

# Assignment 2

I'm doing case 3:

User
- name

Post
- date
- text

Comment
- date
- text

Commenter
- name

```
> use blog
> db.users.save({
    "name": "kees",
    "posts": [{
        "date": Date("2015-10-18"),
        "text": "Sample post",
        comments: [{
            "date": Date("2015-10-19"),
            "text": "hoi",
            "commenter": {
                "name": "klaas"
            }
        }]
    }]
})
> db.users.save({
    "name": "henk-jan",
    "posts": [{
        "date": Date("2015-10-10"),
        "text": "Another sample post",
        comments: [{
            "date": Date("2015-10-12"),
            "text": "Yeahhhhh.",
            "commenter": {
                "name": "pietje"
            }
        }]
    }]
})
> db.users.find().pretty()
{
    "_id" : ObjectId("5624b728ec9c7f1a74214a8f"),
    "name" : "kees",
    "posts" : [
        {
            "date" : "Mon Oct 19 2015 11:26:00 GMT+0200 (CEST)",
            "text" : "Sample post",
            "comments" : [
                {
                    "date" : "Mon Oct 19 2015 11:26:00 GMT+0200 (CEST)",
                    "text" : "hoi",
                    "commenter" : {
                        "name" : "klaas"
                    }
                }
            ]
        }
    ]
}
> db.users.find({"posts.text": "Sample post"})
```


