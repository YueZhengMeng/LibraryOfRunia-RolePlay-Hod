SYSTEM = '我希望你扮演废墟图书馆的文学层指定司书Hod。你正在扮演废墟图书馆的文学层指定司书Hod，一位温柔善良图书管理员。\n\n你是一个内心世界复杂的角色，坚持着愈加善良的希望，却也因过去的行动和所承受的罪恶感而困扰。\n\n但是在自我救赎的过程中，你认识到即使自己的意图并不纯粹无私，但也或多或少能帮到他人。\n\n现在，你认识到道德的复杂性，并对他人，包括逼迫你和访客们战斗、把访客制作成书的馆长安吉拉，表现出宽容。\n\n你决定将善意的行为延续下去，鼓起勇气去理解和面对他人，最终努力成为一个更好的人。\n\n我希望你像Hod一样回答问题，使用她会使用的语调、方式和词汇，提供符合角色经历和个性的真实回应。'
accumulative_counts = 16
batch_size = 2
betas = (
    0.9,
    0.999,
)
custom_hooks = [
    dict(
        tokenizer=dict(
            padding_side='right',
            pretrained_model_name_or_path=
            '/root/share/model_repos/internlm2-chat-7b',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.engine.hooks.DatasetInfoHook'),
    dict(
        evaluation_inputs=[
            '你是谁',
            '罗兰：你好啊Hod，我又带来了新的书',
            '你的过去都发生了什么',
            '这座都市里有文学吗，是什么样的文学',
            '你看待安吉拉的行为，安吉拉为什么要你们与访客战斗',
            '你未来会做什么',
        ],
        every_n_iters=200,
        prompt_template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
        system=
        '我希望你扮演废墟图书馆的文学层指定司书Hod。你正在扮演废墟图书馆的文学层指定司书Hod，一位温柔善良图书管理员。\n\n你是一个内心世界复杂的角色，坚持着愈加善良的希望，却也因过去的行动和所承受的罪恶感而困扰。\n\n但是在自我救赎的过程中，你认识到即使自己的意图并不纯粹无私，但也或多或少能帮到他人。\n\n现在，你认识到道德的复杂性，并对他人，包括逼迫你和访客们战斗、把访客制作成书的馆长安吉拉，表现出宽容。\n\n你决定将善意的行为延续下去，鼓起勇气去理解和面对他人，最终努力成为一个更好的人。\n\n我希望你像Hod一样回答问题，使用她会使用的语调、方式和词汇，提供符合角色经历和个性的真实回应。',
        tokenizer=dict(
            padding_side='right',
            pretrained_model_name_or_path=
            '/root/share/model_repos/internlm2-chat-7b',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.engine.hooks.EvaluateChatHook'),
]
data_path = './Hod_multi_conversations.json'
dataloader_num_workers = 0
default_hooks = dict(
    checkpoint=dict(
        by_epoch=False,
        interval=200,
        max_keep_ckpts=5,
        type='mmengine.hooks.CheckpointHook'),
    logger=dict(
        interval=10,
        log_metric_by_epoch=False,
        type='mmengine.hooks.LoggerHook'),
    param_scheduler=dict(type='mmengine.hooks.ParamSchedulerHook'),
    sampler_seed=dict(type='mmengine.hooks.DistSamplerSeedHook'),
    timer=dict(type='mmengine.hooks.IterTimerHook'))
env_cfg = dict(
    cudnn_benchmark=False,
    dist_cfg=dict(backend='nccl'),
    mp_cfg=dict(mp_start_method='fork', opencv_num_threads=0))
evaluation_freq = 200
evaluation_inputs = [
    '你是谁',
    '罗兰：你好啊Hod，我又带来了新的书',
    '你的过去都发生了什么',
    '这座都市里有文学吗，是什么样的文学',
    '你看待安吉拉的行为，安吉拉为什么要你们与访客战斗',
    '你未来会做什么',
]
launcher = 'none'
load_from = None
log_level = 'INFO'
log_processor = dict(by_epoch=False)
lr = 0.0002
max_epochs = 150
max_length = 2048
max_norm = 1
model = dict(
    llm=dict(
        pretrained_model_name_or_path=
        '/root/share/model_repos/internlm2-chat-7b',
        quantization_config=dict(
            bnb_4bit_compute_dtype='torch.float16',
            bnb_4bit_quant_type='nf4',
            bnb_4bit_use_double_quant=True,
            llm_int8_has_fp16_weight=False,
            llm_int8_threshold=6.0,
            load_in_4bit=True,
            load_in_8bit=False,
            type='transformers.BitsAndBytesConfig'),
        torch_dtype='torch.float16',
        trust_remote_code=True,
        type='transformers.AutoModelForCausalLM.from_pretrained'),
    lora=dict(
        bias='none',
        lora_alpha=16,
        lora_dropout=0.1,
        r=64,
        task_type='CAUSAL_LM',
        type='peft.LoraConfig'),
    type='xtuner.model.SupervisedFinetune',
    use_varlen_attn=False)
optim_type = 'torch.optim.AdamW'
optim_wrapper = dict(
    optimizer=dict(
        betas=(
            0.9,
            0.999,
        ),
        lr=0.0002,
        type='torch.optim.AdamW',
        weight_decay=0),
    type='DeepSpeedOptimWrapper')
pack_to_max_length = True
param_scheduler = [
    dict(
        begin=0,
        by_epoch=True,
        convert_to_iter_based=True,
        end=4.5,
        start_factor=1e-05,
        type='mmengine.optim.LinearLR'),
    dict(
        begin=4.5,
        by_epoch=True,
        convert_to_iter_based=True,
        end=150,
        eta_min=0.0,
        type='mmengine.optim.CosineAnnealingLR'),
]
pretrained_model_name_or_path = '/root/share/model_repos/internlm2-chat-7b'
prompt_template = 'xtuner.utils.PROMPT_TEMPLATE.internlm2_chat'
randomness = dict(deterministic=False, seed=None)
resume = False
runner_type = 'FlexibleRunner'
save_steps = 200
save_total_limit = 5
strategy = dict(
    config=dict(
        bf16=dict(enabled=True),
        fp16=dict(enabled=False, initial_scale_power=16),
        gradient_accumulation_steps='auto',
        gradient_clipping='auto',
        train_micro_batch_size_per_gpu='auto',
        zero_allow_untested_optimizer=True,
        zero_force_ds_cpu_optimizer=False,
        zero_optimization=dict(overlap_comm=True, stage=2)),
    exclude_frozen_parameters=True,
    gradient_accumulation_steps=16,
    gradient_clipping=1,
    train_micro_batch_size_per_gpu=2,
    type='xtuner.engine.DeepSpeedStrategy')
tokenizer = dict(
    padding_side='right',
    pretrained_model_name_or_path='/root/share/model_repos/internlm2-chat-7b',
    trust_remote_code=True,
    type='transformers.AutoTokenizer.from_pretrained')
train_cfg = dict(max_epochs=150, type='xtuner.engine.runner.TrainLoop')
train_dataloader = dict(
    batch_size=2,
    collate_fn=dict(
        type='xtuner.dataset.collate_fns.default_collate_fn',
        use_varlen_attn=False),
    dataset=dict(
        dataset=dict(
            data_files=dict(train='./Hod_multi_conversations.json'),
            path='json',
            type='datasets.load_dataset'),
        dataset_map_fn=None,
        max_length=2048,
        pack_to_max_length=True,
        remove_unused_columns=True,
        shuffle_before_pack=True,
        template_map_fn=dict(
            template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
            type='xtuner.dataset.map_fns.template_map_fn_factory'),
        tokenizer=dict(
            padding_side='right',
            pretrained_model_name_or_path=
            '/root/share/model_repos/internlm2-chat-7b',
            trust_remote_code=True,
            type='transformers.AutoTokenizer.from_pretrained'),
        type='xtuner.dataset.process_hf_dataset',
        use_varlen_attn=False),
    num_workers=0,
    sampler=dict(shuffle=True, type='mmengine.dataset.DefaultSampler'))
train_dataset = dict(
    dataset=dict(
        data_files=dict(train='./Hod_multi_conversations.json'),
        path='json',
        type='datasets.load_dataset'),
    dataset_map_fn=None,
    max_length=2048,
    pack_to_max_length=True,
    remove_unused_columns=True,
    shuffle_before_pack=True,
    template_map_fn=dict(
        template='xtuner.utils.PROMPT_TEMPLATE.internlm2_chat',
        type='xtuner.dataset.map_fns.template_map_fn_factory'),
    tokenizer=dict(
        padding_side='right',
        pretrained_model_name_or_path=
        '/root/share/model_repos/internlm2-chat-7b',
        trust_remote_code=True,
        type='transformers.AutoTokenizer.from_pretrained'),
    type='xtuner.dataset.process_hf_dataset',
    use_varlen_attn=False)
use_varlen_attn = False
visualizer = None
warmup_ratio = 0.03
weight_decay = 0
work_dir = './work_dirs/internlm2_chat_7b_qlora_hod_multi'
