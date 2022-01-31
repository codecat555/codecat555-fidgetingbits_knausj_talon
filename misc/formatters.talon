#Note: Appending $ will anchor the command
#provide both anchored and unachored commands via 'over'
#say <user.text>: user.insert_formatted(text, "NOOP")
#phrase <user.text> over: user.insert_formatted(text, "NOOP")
{user.prose_formatter} <user.prose>$: user.insert_formatted(prose, prose_formatter)
{user.prose_formatter} <user.prose> over: user.insert_formatted(prose, prose_formatter)
<user.format_text>+$: user.insert_many(format_text_list)
<user.format_text>+ [over]: user.insert_many(format_text_list)
<user.formatters> that: user.formatters_reformat_selection(user.formatters)
(only|lonely) <user.word>: user.insert_formatted(user.word, "NOOP")
just <user.word>: user.insert_formatted(user.word, "NOOP")
format help: user.formatters_help_toggle()
recent list: user.toggle_phrase_history()
recent close: user.phrase_history_hide()
recent repeat <number_small>: insert(user.get_recent_phrase(number_small))
recent copy <number_small>: clip.set_text(user.get_recent_phrase(number_small))
select that: user.select_last_phrase()
before that: user.before_last_phrase()
(nope that | scratch that): user.clear_last_phrase()
nope that was <user.formatters>: user.formatters_reformat_last(formatters)

# @rntz recommendation on slack
#<user.format_text>+ [over]: user.insert_many(format_text_list)
#(<user.formatters> exactly | phrase) <user.text>$:
#  user.insert_formatted(text, formatters or "NOOP")
