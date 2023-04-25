# Generated by Django 4.1 on 2023-04-22 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32, verbose_name="部门名称")),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32, verbose_name="岗位名称")),
                (
                    "level",
                    models.SmallIntegerField(
                        choices=[(1, "1级"), (2, "2级"), (3, "3级"), (4, "4级")],
                        default=1,
                        verbose_name="级别",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Shop",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=32, verbose_name="店铺名称")),
                ("sever_ip", models.CharField(max_length=32, verbose_name="服务器IP")),
                ("create_date", models.DateTimeField(verbose_name="添加时间")),
                ("update_date", models.DateTimeField(verbose_name="更新时间")),
            ],
        ),
        migrations.CreateModel(
            name="Site",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "site",
                    models.SmallIntegerField(
                        choices=[(1, "de"), (2, "cn"), (3, "usa"), (4, "ca")],
                        default=1,
                        verbose_name="站点",
                    ),
                ),
                ("front_host", models.CharField(max_length=32, verbose_name="前台host")),
                ("back_host", models.CharField(max_length=32, verbose_name="后台host")),
                ("zip_code", models.CharField(max_length=32, verbose_name="邮编")),
                ("create_date", models.DateTimeField(verbose_name="添加时间")),
                ("update_date", models.DateTimeField(verbose_name="更新时间")),
            ],
        ),
        migrations.CreateModel(
            name="Staff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nick", models.CharField(max_length=32, verbose_name="昵称")),
                ("name", models.CharField(max_length=32, verbose_name="姓名")),
                ("mobile", models.CharField(max_length=32, verbose_name="手机号")),
                ("dingding_key", models.CharField(max_length=32, verbose_name="钉钉key")),
                (
                    "gender",
                    models.SmallIntegerField(
                        choices=[(1, "男"), (2, "女")], verbose_name="性别"
                    ),
                ),
                ("start_date", models.DateTimeField(verbose_name="入职时间")),
                ("create_date", models.DateTimeField(verbose_name="添加时间")),
                ("update_date", models.DateTimeField(verbose_name="更新时间")),
                (
                    "depart",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app01.department",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app01.post"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Asin",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("asin", models.CharField(max_length=32, verbose_name="Asin")),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "未爬取"), (2, "已成功爬取"), (3, "正在爬取"), (4, "爬取失败")],
                        default=1,
                        verbose_name="状态",
                    ),
                ),
                ("create_date", models.DateTimeField(verbose_name="添加时间")),
                ("update_date", models.DateTimeField(verbose_name="更新时间")),
                (
                    "shop",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app01.shop"
                    ),
                ),
                (
                    "site",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app01.site"
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app01.staff"
                    ),
                ),
            ],
        ),
    ]