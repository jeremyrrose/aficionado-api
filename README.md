# Aficionado API

Forked from [Besrat Z.'s Capture API](https://github.com/bzerehaimanot8/p4backend).

## User Stories

### User 1

Tara is a sculptor who wants to display images of her works in a profile with her contact information. She would like for potential customers to be able to follow her work.

### User 2

Sara has money to burn and loves visiting art galleries. She would like to see artists portfolios to consider purchases and follow artists' work.

## Models

### User
```python
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### CreatorProfile
```python
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="creators")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### CustomerProfile
```python
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    prospect_list = models.ManyToManyField(CreatorProfile, related_name='supporters', blank=True)
```

### Image
```python
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image_url = models.URLField(max_length=500)
    creator_profile = models.ForeignKey(CreatorProfile, related_name='images', on_delete=models.CASCADE)
```

### Tag
```python
    tag_name = models.CharField(max_length=500)
```

## Endpoints

### Auth
```python
    url(r'^users/$', UserListViewSet.as_view({'get': 'list'}), name='user_list'),
    url(r'^users/register/$', RegistrationAPIView.as_view(), name='register'),
    url(r'^users/login/$', LoginAPIView.as_view(), name='login'),
```

### API
```python
router.register('creators', CreatorProfileViewSet, basename='creators')
router.register('customers', CustomerProfileViewSet, basename='customers')
router.register('images', ImageViewSet, basename='images')

custom_urlpatterns = [
    url(r'creators/(?P<creator_pk>\d+)/photos$', CreatorImages.as_view(),
        name='creator_images'),
    url(r'tags/(?P<tag_pk>\d+)/$', TagCreators.as_view(), name='creators_by_tag')
]
```
