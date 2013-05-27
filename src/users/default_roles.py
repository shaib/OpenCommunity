from django.utils.translation import ugettext_lazy as _

class DefaultRoles(object):

    VIEWER = 'viewer'
    OBSERVER = 'observer'
    PROPOSER = 'proposer'
    CONTRIBUTOR = 'contributor'
    EDITOR = 'editor'
    OPERATOR = 'operator'
    DECIDER = 'decider'
    MANAGER = 'manager'

    permissions = {}

    permissions[VIEWER] = [
                           'issues.viewclosed_issue',
                           'issues.viewclosed_proposal',
                           'meeting.view_meeting',
                           ]

    permissions[OBSERVER] = permissions[VIEWER] + [
                           'issues.viewopen_issue',
                           'issues.viewopen_proposal',
                           'communities.viewupcoming_community',
                          ]

    permissions[PROPOSER] = permissions[OBSERVER] + [
                           'issues.add_proposal',
                           'communities.viewupcoming_community',
                          ]

    permissions[CONTRIBUTOR] = permissions[PROPOSER] + [
                           'issues.add_issue',
                          ]

    permissions[EDITOR] = permissions[CONTRIBUTOR] + [
                           'issues.editopen_issue',
                           'issues.editopen_proposal',
                           'issues.edittask_proposal',
                          ]

    permissions[OPERATOR] = permissions[CONTRIBUTOR] + [
                           'issues.add_issuecomment',
                           'issues.edittask_proposal',
                           'community.editupcoming_community',
                           'community.editparticipants_community',
                           'community.editsummary_community', # ???
                           'community.invite_member',
                          ]

    permissions[DECIDER] = permissions[OPERATOR] + [
                           'issues.editopen_issuecomment',
                           'community.editagenda_community',
                           'meetings.add_meeting',  # Close!
                          ]

    permissions[MANAGER] = permissions[DECIDER] + [
                           'issues.editopen_issue',
                           'issues.editclosed_issue',
                           'issues.editopen_proposal',
                           'issues.editclosed_proposal',
                           'issues.acceptclosed_proposal',
                          ]


class DefaultGroups(object):
    MEMBER = "member"
    BOARD = "board"
    SECRETARY = "secretary"
    CHAIRMAN = "chairman"

    permissions = {}

    permissions[MEMBER] = set(DefaultRoles.permissions[DefaultRoles.VIEWER])
    permissions[BOARD] = set(DefaultRoles.permissions[DefaultRoles.PROPOSER])
    permissions[SECRETARY] = set(DefaultRoles.permissions[DefaultRoles.OPERATOR])
    permissions[CHAIRMAN] = set(DefaultRoles.permissions[DefaultRoles.DECIDER] +
                                DefaultRoles.permissions[DefaultRoles.MANAGER])
    CHOICES = (
                (MEMBER, _("member")),
                (BOARD, _("board")),
                (SECRETARY, _("secretary")),
                (CHAIRMAN, _("chairman")),
               )

