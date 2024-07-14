def global_context(request):
    FAKE_DB_COMPANIES = [
        f"http://picsum.photos/id/{id}/100/80" for id in range(50,58)
    ]
    hero_content = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Error qui facilis corrupti ex tempora repellat blanditiis deleniti molestiae molestias placeat!"
    return dict(
        FAKE_DB_COMPANIES = FAKE_DB_COMPANIES,
        hero_content = hero_content,
    )