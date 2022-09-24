from graphene import ObjectType, String, Int, Field, Mutation,Boolean, List
from seeker.models import *
from .all_query_types import *


# region seeker mutations
class CreateSeeker(Mutation):
    class Arguments:
        first_name    = String(required=True)
        middle_name   = String(required=False)
        last_name     = String(required=True)
        date_of_birth = String(required=True)
        email         = String(required=True)
        phone         = Int(required=True)

    seeker = Field(SeekerType)

    def mutate(self,info, first_name,middle_name,last_name,date_of_birth,email,phone):
        seeker = Seeker(
            first_name    = first_name,
            middle_name   = middle_name,
            last_name     = last_name,
            date_of_birth = date_of_birth,
            email         = email,
            phone         = phone
            )
        seeker.save()
        return CreateSeeker(seeker=seeker)


class UpdateSeeker(Mutation):
    class Arguments:
        id            = Int(required=True)
        first_name    = String(required=False)
        middle_name   = String(required=False)
        last_name     = String(required=False)
        date_of_birth = String(required=False)
        email         = String(required=False)
        phone         = Int(required=False)

    seeker = Field(SeekerType)

    def mutate(self,info, id, first_name,middle_name,last_name,date_of_birth,email,phone):
        seeker = Seeker.objects.get(id=id)

        seeker.first_name    = first_name
        seeker.middle_name   = middle_name
        seeker.last_name     = last_name
        seeker.date_of_birth = date_of_birth
        seeker.email         = email
        seeker.phone         = phone

        seeker.save()
        return UpdateSeeker(seeker=seeker)


class DeleteSeeker(Mutation):
    class Arguments:
        id = Int(required=True)

    seeker = Field(SeekerType)
    success = Boolean()

    def mutate(self,info, id):
        seeker = Seeker.objects.get(id=id)
        seeker.delete()
        return DeleteSeeker(seeker=seeker, success=True)
# endregion seeker mutations


# region education mutations
class CreateEducation(Mutation):
    class Arguments:
        start_date    = String(required=True)
        end_date      = String(required=True)
        institution   = String(required=True)
        certification = String(required=False)

    education = Field(EducationType)

    def mutate(self,info, start_date,end_date,institution,certification):
        education = Education(
            start_date    = start_date,
            end_date      = end_date,
            institution   = institution,
            certification = certification
            )
        education.save()
        return CreateEducation(education=education)


class UpdateEducation(Mutation):
    class Arguments:
        id            = Int(required=True)
        start_date    = String(required=False)
        end_date      = String(required=False)
        institution   = String(required=False)
        certification = String(required=False)

    education = Field(EducationType)

    def mutate(self,info, id, start_date,end_date,institution,certification):
        education = Education.objects.get(id=id)

        education.start_date    = start_date
        education.end_date      = end_date
        education.institution   = institution
        education.certification = certification

        education.save()
        return UpdateEducation(education=education)


class DeleteEducation(Mutation):
    class Arguments:
        id = Int(required=True)

    education = Field(EducationType)
    success = Boolean()

    def mutate(self,info, id):
        education = Education.objects.get(id=id)
        education.delete()
        return DeleteEducation(education=education, success=True)
# endregion education mutations


# region skills mutations
class CreateSkill(Mutation):
    class Arguments:
        name = String(required=True)

    skill = Field(SkillsType)

    def mutate(self,info, name):
        skill = Skill(
            name = name
            )
        skill.save()
        return CreateSkill(skill=skill)


class UpdateSkill(Mutation):
    class Arguments:
        id   = Int(required=True)
        name = String(required=False)

    skill = Field(SkillsType)

    def mutate(self,info, id, name):
        skill = Skill.objects.get(id=id)

        skill.name = name

        skill.save()
        return UpdateSkill(skill=skill)


class DeleteSkill(Mutation):
    class Arguments:
        id = Int(required=True)

    skill = Field(SkillsType)
    success = Boolean()

    def mutate(self,info, id):
        skill = Skill.objects.get(id=id)
        skill.delete()
        return DeleteSkill(skill=skill, success=True)
# endregion skills mutations


# region experience mutations
class CreateExperience(Mutation):
    class Arguments:
        start_date    = String(required=True)
        end_date      = String(required=True)
        company       = String(required=True)
        title         = String(required=True)
        description   = String(required=False)

    experience = Field(ExperienceType)

    def mutate(self,info, start_date,end_date,company,title,description):
        experience = Experience(
            start_date    = start_date,
            end_date      = end_date,
            company       = company,
            title         = title,
            description   = description
            )
        experience.save()
        return CreateExperience(experience=experience)

class UpdateExperience(Mutation):
    class Arguments:
        id            = Int(required=True)
        start_date    = String(required=False)
        end_date      = String(required=False)
        company       = String(required=False)
        title         = String(required=False)
        description   = String(required=False)

    experience = Field(ExperienceType)

    def mutate(self,info, id, start_date,end_date,company,title,description):
        experience = Experience.objects.get(id=id)

        experience.start_date    = start_date
        experience.end_date      = end_date
        experience.company       = company
        experience.title         = title
        experience.description   = description

        experience.save()
        return UpdateExperience(experience=experience)


class DeleteExperience(Mutation):
    class Arguments:
        id = Int(required=True)

    experience = Field(ExperienceType)
    success = Boolean()

    def mutate(self,info, id):
        experience = Experience.objects.get(id=id)
        experience.delete()
        return DeleteExperience(experience=experience, success=True)
# endregion experience mutations


# region seeker profile mutations

# endregion seeker profile mutations