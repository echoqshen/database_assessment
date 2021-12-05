CREATE TABLE "gym" (
    "gym_ID" INTEGER   NOT NULL,
    "gym_Name" VARCHAR   NOT NULL,
    "address" VARCHAR   NOT NULL,
    "city" VARCHAR   NOT NULL,
    "zipcode" VARCHAR   NOT NULL,
    CONSTRAINT "pk_gym" PRIMARY KEY (
        "gym_ID"
     )
);

CREATE TABLE "trainers" (
    "trainer_id" INTEGER   NOT NULL,
    "gym_id" INTEGER   NOT NULL,
    "first_name" VARCHAR   NOT NULL,
    "last_name" VARCHAR   NOT NULL,
    CONSTRAINT "pk_trainers" PRIMARY KEY (
        "trainer_id"
     )
);

CREATE TABLE "members" (
    "member_id" INTEGER   NOT NULL,
    "gym_id" INTEGER   NOT NULL,
    "trainer_id" INTEGER   NOT NULL,
    "first_name" VARCHAR   NOT NULL,
    "last_name" VARCHAR   NOT NULL,
    "address" VARCHAR   NOT NULL,
    "city" VARCHAR   NOT NULL,
    CONSTRAINT "pk_members" PRIMARY KEY (
        "member_id"
     )
);

CREATE TABLE "payments" (
    "payment_id" INTEGER   NOT NULL,
    "member_id" INTEGER   NOT NULL,
    "creditcard_info" INTEGER   NOT NULL,
    "billing_zip" INTEGER   NOT NULL,
    CONSTRAINT "pk_payments" PRIMARY KEY (
        "payment_id"
     )
);

CREATE TABLE "classes" (
    "class_id" integer   NOT NULL,
    "trainer_id" integer   NOT NULL,
    "gym_id" integer   NOT NULL,
    "class_name" varchar   NOT NULL,
    "commission_percentage" numeric   NOT NULL,
    CONSTRAINT "pk_classes" PRIMARY KEY (
        "class_id"
     )
);

CREATE TABLE "class_attendance" (
    "member_id" INTEGER   NOT NULL,
    "class_id" integer   NOT NULL,
    CONSTRAINT "pk_class_attendance" PRIMARY KEY (
        "member_id","class_id"
     )
);

ALTER TABLE "trainers" ADD CONSTRAINT "fk_trainers_gym_id" FOREIGN KEY("gym_id")
REFERENCES "gym" ("gym_ID");